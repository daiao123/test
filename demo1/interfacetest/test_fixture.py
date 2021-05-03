
class Testlogin:

    def test_01_fixture(self):
        print("第一个pytest")

    # def test_02_fixture(self):
    #     print("第二个pytest")

    def test_03_fixture(self, my_fixture):
        print("第三个pytest" + str(my_fixture))

# class Testlogin2:
#
#     def test_04_fixture(self, my_fixture):
#         print("第4个pytest")
#
#     def test_05_fixture(self):
#         print("第5个pytest")
#
#     def test_06_fixture(self, my_fixture):
#         print("第6个pytest")




