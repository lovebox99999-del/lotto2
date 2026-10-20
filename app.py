import random
import time
import streamlit as st

# 페이지 설정
st.set_page_config(page_title="대한민국 로또 번호 생성기", page_icon="🎲", layout="centered")

def get_ball_color(number):
    """로또 공 번호 구간별 한국 공식 색상 반환"""
    if number <= 10:
        return "#fbc400" # 노란색 (1~10)
    elif number <= 20:
        return "#69c8f2" # 파란색 (11~20)
    elif number <= 30:
        return "#ff7272" # 빨간색 (21~30)
    elif number <= 40:
        return "#aaaaaa" # 회색 (31~40)
    else:
        return "#b0d840" # 초록색 (41~45)

def make_ball_html(num, is_bonus=False):
    """공 하나를 그리는 HTML 태그 생성"""
    color = get_ball_color(num)
    label = "보너스" if is_bonus else ""
    return f"""
    <div style='display: inline-block; text-align: center; margin: 0 4px;'>
        <div style='
            width: 45px;
            height: 45px;
            line-height: 45px;
            border-radius: 50%;
            background-color: {color};
            color: #fff;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        '>{num}</div>
    </div>
    """

st.title("🎲 대한민국 표준 로또 6/45 추첨기")
st.write("버튼을 누르면 행운의 번호가 추첨됩니다!")

# 추첨 버튼
if st.button("로또 번호 뽑기", type="primary"):
    all_numbers = list(range(1, 46))
    
    # 1. 6개 당첨 번호 추출 및 정렬
    main_numbers = sorted(random.sample(all_numbers, 6))
    
    # 2. 보너스 번호 1개 추출 (중복 불가)
    remaining_numbers = [n for n in all_numbers if n not in main_numbers]
    bonus_number = random.choice(remaining_numbers)
    
    # 결과를 보여줄 빈 공간(Placeholder) 생성
    result_container = st.empty()
    
    # 애니메이션 효과 (하나씩 띄우기)
    drawn_main = []
    for num in main_numbers:
        drawn_main.append(num)
        balls_html = "".join([make_ball_html(n) for n in drawn_main])
        result_container.markdown(f"<div style='display: flex; align-items: center;'>{balls_html}</div>", unsafe_allow_html=True)
        time.sleep(0.3)
    
    # 마지막에 보너스 번호 추가
    time.sleep(0.3)
    main_balls_html = "".join([make_ball_html(n) for n in main_numbers])
    plus_sign_html = "<span style='font-size:24px; font-weight:bold; margin: 0 10px;'>+</span>"
    bonus_ball_html = make_ball_html(bonus_number, is_bonus=True)
    
    final_html = f"""
    <div style='display: flex; align-items: center; margin-top: 10px;'>
        {main_balls_html}
        {plus_sign_html}
        {bonus_ball_html}
    </div>
    """
    result_container.markdown(final_html, unsafe_allow_html=True)
    st.success("✨ 대박을 기원합니다! ✨")
