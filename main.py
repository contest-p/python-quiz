def read_number(prompt, maximum):
    """1부터 maximum 사이의 번호를 받을 때까지 다시 묻는다."""
    while True:
        text = input(prompt).strip()

        try:
            number = int(text)
            if 1 <= number <= maximum:
                return number
        except ValueError:
            # 숫자 변환에 실패하면 아래 공통 안내를 사용한다.
            pass

        print(f"1부터 {maximum}까지의 번호를 입력해 주세요.")


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