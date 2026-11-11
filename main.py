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

class QuizGame:
    def __init__(self):
        self.quizzes = create_default_quizzes()
        self.best_score = None
    def play_quiz(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없어요.")
            return

        correct_count = 0

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[문제 {number}]")
            quiz.show()

            selected = read_number("정답: ", len(quiz.choices))
            if quiz.is_correct(selected):
                print("정답입니다!!!!!!!!!!!!!!!!")
                correct_count += 1
            else:
                print("오답이에요................")

        score = correct_count / len(self.quizzes) * 100
        print(f"\n결과: {len(self.quizzes)}문제 중 {correct_count}문제 정답 ({score:.1f}점)")
        return score

    def add_quiz(self):
        print("\n=== 퀴즈 추가 ===")

        question = input("문제를 입력하세요: ").strip()
        while not question:
            print("문제를 비워 둘 수 없어요.")
            question = input("문제를 입력하세요: ").strip()

        choices = []
        for number in range(1, 5):
            choice = input(f"선택지 {number}: ").strip()
            while not choice:
                print("선택지를 비워 둘 수 없어요.")
                choice = input(f"선택지 {number}: ").strip()
            choices.append(choice)

        answer = read_number("정답 번호 (1~4): ", 4)

        self.quizzes.append(Quiz(question, choices, answer))
        print("퀴즈가 추가되었습니다!")

    def show_quiz_list(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없어요.")
            return

        print(f"\n=== 등록된 퀴즈 목록 (총 {len(self.quizzes)}개) ===")
        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"{number}. {quiz.question}")


    def run(self):

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

            if choice == 1:
                score = self.play_quiz()
                if score is not None:
                    if self.best_score is None or score > self.best_score:
                        self.best_score = score
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.show_quiz_list()
            elif choice == 4:
                if self.best_score is None:
                    print("아직 퀴즈를 풀지 않았어요.")
                else:
                    print(f"최고 점수: {self.best_score:.1f}점")
            else:
                print(f"{choice}번을 선택했어요.")


if __name__ == "__main__":
    game = QuizGame()
    game.run()
