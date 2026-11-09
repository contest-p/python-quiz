class Quiz:
    # 퀴즈 한 문제를 담는 카드 양식이에요.

    def __init__(self, question, choices, answer):
        # 카드를 만들 때 받은 문제, 선택지, 정답을 이 카드(self)에 저장해요.
        self.question = question
        self.choices = choices
        self.answer = answer

    def show(self):
        # 문제를 보여주고 선택지에 1번부터 번호를 붙여요.
        print(self.question)
        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")

    def is_correct(self, selected_number):
        # 고른 번호가 정답과 같으면 True, 다르면 False를 돌려줘요.
        return selected_number == self.answer


def read_number(prompt, maximum):
    # 1부터 maximum까지의 번호가 들어올 때까지 다시 물어요.
    while True:
        text = input(prompt).strip()

        try:
            number = int(text)
            if 1 <= number <= maximum:
                return number
        except ValueError:
            pass

        print(f"1부터 {maximum}까지의 번호를 입력해 주세요.")


def main():
    # 메뉴를 보여주고, 5번을 선택하면 반복을 끝내요.
    while True:
        print("\n=== 상식 퀴즈 게임 ===")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")

        choice = read_number("선택: ", 5)

        if choice == 5:
            print("게임을 종료합니다.")
            break

        print(f"{choice}번을 선택했어요.")


if __name__ == "__main__":
    # python main.py로 실행하면 여기서 메뉴를 시작해요.
    main()