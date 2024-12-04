# 원소 및 스킬 정의
elements = ['불', '물', '공기', '흙']
skills = ['Q', 'W', 'E', 'R']
skill_to_element = {skill: None for skill in skills}  # 스킬-원소 초기화
selected_skills = []  # 선택된 스킬 리스트

# 수동 난수 함수 (이전 코드에서와 동일)
def manual_random_choice(lst):
    total_elements = len(lst)
    if total_elements == 0:
        return None
    index = (hash(str(lst)) % total_elements)
    return lst[index]

# 원소를 스킬에 무작위 할당
def assign_random_element(skill):
    if skill in skill_to_element:
        if skill_to_element[skill] is None:  # 스킬이 비어있다면
            available_elements = [elem for elem in elements if elem not in skill_to_element.values()]
            if available_elements:
                chosen_element = manual_random_choice(available_elements)
                skill_to_element[skill] = chosen_element
                return f"스킬 {skill}에 원소 '{chosen_element}'이(가) 최초로 할당되었습니다."
            else:
                return "모든 원소가 이미 사용되었습니다."
        else:
            if skill not in selected_skills:  # 선택되지 않은 경우
                selected_skills.append(skill)  # 선택된 스킬 추가
                return f"스킬 {skill}이(가) [선택됨] 상태로 전환되었습니다."
            else:  # 이미 선택된 경우 다시 선택하면 [선택안됨] 상태로 변경
                selected_skills.remove(skill)
                return f"스킬 {skill}이(가) [선택안됨] 상태로 변경되었습니다."
    else:
        return "유효하지 않은 스킬입니다."

# 선택된 스킬 및 원소 출력
def print_selected_skills():
    for skill in skills:
        status = "선택됨" if skill in selected_skills else "선택안됨"
        element = skill_to_element[skill] if skill_to_element[skill] else "비어 있음"
        print(f" {skill}: [{status}] - 원소: {element}")

# 스킬 초기화 (발사 후)
def reset_skills():
    for skill in selected_skills:
        skill_to_element[skill] = None  # 원소 초기화
    selected_skills.clear()  # 선택된 스킬 리스트 초기화
    print("모든 선택된 스킬이 초기화되었습니다.")

# G키를 눌렀을 때, 선택된 스킬 조합 발사 및 초기화
def fire_skills():
    if len(selected_skills) >= 2:  # 최소 두 개의 스킬이 선택된 경우
        skill_combo = " + ".join(selected_skills)
        print(f"{skill_combo} 발사!")
        reset_skills()  # 발사 후 스킬 초기화
    else:
        print("두 개 이상의 스킬을 선택해야 발사할 수 있습니다.")

# 사용자 스킬 선택 및 입력 받기
def user_select_skill():
    print("사용 가능한 스킬: Q, W, E, R")
    user_choice = input("사용할 스킬을 입력하세요: ").upper()
    print("==========================================================")
    
    if user_choice == 'F':
        print_selected_skills()
    elif user_choice == 'G':
        fire_skills()
    elif user_choice in skills:
        print(assign_random_element(user_choice))
    else:
        print("유효하지 않은 입력입니다.")

# 반복 실행
def main():
    while True:
        user_select_skill()

# 실행
main()
