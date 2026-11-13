# ==============================================================================
# definition.rpy : 등장인물 및 전역 상태 정의
# ==============================================================================

init python:
    # 텍스트 전용 오디오 채널 등록
    renpy.music.register_channel("type_sfx", mixer="sfx", loop=True)

    def play_typing_sound(event, interact=True, **kwargs):
        if not interact:
            return

        # 글자가 화면에 찍히기 시작할 때 -> 타건음 재생
        if event == "show":
            renpy.music.play("audio/keyboard.ogg", channel="type_sfx", loop=True)

        # 타이핑이 끝났거나 클릭으로 스킵했을 때 -> 즉시 정지
        elif event in ("slow_done", "end"):
            renpy.music.stop(channel="type_sfx", fadeout=0.1)

    # 모든 캐릭터(NVL 포함)에 타건음 콜백을 자동 적용
    config.all_character_callbacks.append(play_typing_sound)

# 시스템 및 독백
define sys = Character(None, italic=True)
define nvl_sys = Character(None, kind=nvl)

# 주요 인물
define me = Character("병연", color="#4a90e2")
define ch = Character("천호", color="#50e3c2")
define sj = Character("차서진", color="#ff6b81")
define ok = Character("옥현", color="#a4b0be")
define yh = Character("용화", color="#eccc68")
define st = Character("승태", color="#ffa502")
define t_park = Character("선생님 박", color="#747d8c")

# 챕터 1
define jh = Character("준호", color="#e74c3c")      # 자전거 절도를 주도한 친구
define cop = Character("이 순경", color="#34495e")  # 담당 경찰
define judge = Character("판사", color="#2c3e50")
define lim_teacher = Character("임 선생", color="#27ae60")
define bad_kid_1 = Character("교육생 A", color="#7f8c8d")
define bad_kid_2 = Character("교육생 B", color="#95a5a6")

# 챕터 2~3
define pe_head = Character("체육부장", color="#e67e22")             # 체육부장 선배
define teacher_council = Character("학생회 담당 교사", color="#2980b9")


# 전역 상태 변수
default bike_choice = ""  # 1장 자전거 사건 경찰 통화 응답 ("honest" / "lie")
