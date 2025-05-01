import students as s

def test_case01():
    assert s.add_srudents("001","navya") == "Studen added"

def test_case02():
    assert s.view_students("007") == "Student ID not found"
    
