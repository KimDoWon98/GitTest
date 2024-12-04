class Animal:
    def speak(self):
        print("동물이 소리를 냅니다.")

class Dog(Animal):
    def speak(self):  # 부모 클래스의 speak 메서드를 오버라이딩
        print("강아지가 멍멍 짖습니다.")

my_dog = Dog()
my_dog.speak()  # 오버라이딩된 Dog 클래스의 speak 메서드 호출
