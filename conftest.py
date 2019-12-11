def pytest_report_teststatus(report):
    """ Insert strings that LAVA expects to captur test results.
    """
    # Get pytest test name and remove the 'test_' prefic
    test_name = report.location[2][5:]

    if report.when is 'setup':
        print('\n')
        print('<LAVA_SIGNAL_STARTTC ' + test_name + '>')
    elif report.when is 'call':
        test_result = lava_result_convert(report.outcome)

        print('\n')
        print('<LAVA_SIGNAL_ENDTC ' + test_name + '>')
        print('<LAVA_SIGNAL_TESTCASE TEST_CASAE_ID= ' + test_name + ' RESULT=' + test_result + '>')