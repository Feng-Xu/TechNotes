class Test_with():
    def __enter__(self):
        print("先执行enter")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print('最后正常结束')
        else:
            print('有异常: %s' % exc_tb)
            self.test_help()

    def test_help(self):
        print('help info')


with Test_with() as test:
    print('test_with is running')
    test.test_help()
    #Test_with.test_help(test)
