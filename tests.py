from pre_commit_hooks import check_todos


def test_check_todos_python():
    sample = '''
        # TODO
        def fn():
            """TODO TODO
            a
            b
            c
            todo
            """  # TODO

        def fn2():
            \'\'\'
            another TODO
            \'\'\' # TODO

        #someTODO
        #anotherTODO  # ignore:todo
    '''

    comment_lines = check_todos.get_todo_comments(sample.split("\n"), ".py")
    assert len(comment_lines) == 6
    assert "l2" in comment_lines[0]
    assert "l4" in comment_lines[1]
    assert "l9" in comment_lines[2]
    assert "l13" in comment_lines[3]
    assert "l14" in comment_lines[4]
