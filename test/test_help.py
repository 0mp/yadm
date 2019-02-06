"""Test help"""


def test_missing_command(runner, yadm_y):
    """Run without any command"""
    run = runner(command=yadm_y())
    run.report()
    assert run.failure
    assert run.err == ''
    assert run.out.startswith('Usage: yadm')


def test_help_command(runner, yadm_y):
    """Run with help command"""
    run = runner(command=yadm_y('help'))
    run.report()
    assert run.failure
    assert run.err == ''
    assert run.out.startswith('Usage: yadm')
