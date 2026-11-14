from tennisage.data import _build_url, _opponent_age, _to_date


def test_url_same_for_all_spellings():
    expected = "https://www.tennisabstract.com/jsmatches/SerenaWilliamsCareer.js"
    assert _build_url("serena williams") == expected
    assert _build_url("Serena Williams") == expected
    assert _build_url("SerenaWilliams") == expected


def test_female_opponent_age_from_birth_date():
    age = _opponent_age("19770119", _to_date("19951030"))
    assert abs(age - 18.78) < 0.05


def test_male_opponent_age_used_directly():
    assert _opponent_age("22.264202601", _to_date("20010910")) == 22.264202601


def test_extract_rows_handles_newlines_and_semicolon():
    from tennisage.data import _extract_rows
    js = 'var morematchmx = [["19951030", "A"],\n          ["19970307", "B"]\n          ];'
    assert len(_extract_rows(js)) == 2


def test_find_birth_date_reads_dob_variable():
    from datetime import datetime
    from tennisage.data import _find_birth_date
    profile_js = "    var ht=175;\n    var dob=19810926;\n    var dob_approx=\"\";"
    assert _find_birth_date(profile_js) == datetime(1981, 9, 26)
