class Quiz:
    # 퀴즈 한 문제를 담는 카드 양식이에요.

    def __init__(self, question, choices, answer):
        # 받은 문제, 선택지, 정답 번호를 이 카드에 저장해요.
        self.question = question
        self.choices = choices
        self.answer = answer

    def show(self):
        print(self.question)
        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")

    def is_correct(self, selected_number):
        return selected_number == self.answer


def read_number(prompt, maximum):
    # 1부터 maximum까지의 번호를 받을 때까지 다시 물어요.
    while True:
        text = input(prompt).strip()

        try:
            number = int(text)
            if 1 <= number <= maximum:
                return number
        except ValueError:
            pass

        print(f"1부터 {maximum}까지의 번호를 입력해 주세요.")


def create_default_quizzes():
    # Quiz(...) 하나가 문제 카드 한 장이에요. 마지막 숫자는 정답 번호예요.
    return [
        Quiz("축구 경기에서 한 팀당 경기장에서 뛰는 선수는 총 몇 명일까요?(교체 선수 제외)",
            ["8명", "9명", "10명", "11명"],
            4,),
        Quiz("한글 ㅎ의 이름은?",
            ["히읗", "히읕", "히읃", "히읏"],
            1,),
        Quiz("지구 표면에서 가장 넓은 면적을 차지하고 있는 바다(대양)는 무엇일까요?",
            ["대서양", "인도양", "태평양", "북극해"],
            3,),
        Quiz("조선의 건국자는?",
            ["왕건","이성계","김유신","정몽주"],
            2,),
        Quiz("구글AI 모델의 이름인 '제미나이(Gemini)'는 어떤 별자리의 이름인가요?",
             ["황소 자리","천칭 자리","쌍둥이 자리","처녀자리"],
            3,),
            ]


# STEP 5에서 퀴즈 풀기 함수를 여기에 추가해요.


def main():
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
    main()