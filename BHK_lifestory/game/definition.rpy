# ==============================================================================
# definitions.rpy : 등장인물 및 전역 상태 정의
# ==============================================================================

init python:
    # 텍스트 전용 오디오 채널 등록
    renpy.music.register_channel("type_sfx", mixer="sfx", loop=True)

    def play_typing_sound(event, interact=True, **kwargs):
        if not interact:
            return

        # 글자가 화면에 찍히기 시작할 때 -> 타건음 재생
        if event == "show":
            renpy.music.play("audio/keyboard.mp3", channel="type_sfx", loop=True)

        # 타이핑이 끝났거나 클릭으로 스킵했을 때 -> 즉시 정지
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="type_sfx",fadeout=0.1)

# 시스템 및 독백
define sys = Character(None, italic=True, callback=play_typing_sound)

# 주요 인물 정의
define me = Character("병연", color="#4a90e2", callback=play_typing_sound)
define ch = Character("천호", color="#50e3c2", callback=play_typing_sound)
define sj = Character("차서진", color="#ff6b81", callback=play_typing_sound)
define f1 = Character("옥현", color="#a4b0be", callback=play_typing_sound)
define yh = Character("용화", color="#eccc68", callback=play_typing_sound)
define st = Character("승태", color="#ffa502", callback=play_typing_sound)
define t_park = Character("선생님 박", color="#747d8c", callback=play_typing_sound)
define jh = Character("준호", color="#e74c3c", callback=play_typing_sound)      # 자전거 절도를 주도한 친구
define cop = Character("이 순경", color="#34495e", callback=play_typing_sound)   # 담당 경찰

# 전역 상태 변수
default stat_determination = 0     # 독기 / 멘탈 스탯
default stat_reputation = 50       # 교내 평판 수치
default flag_bald = False          # 삭발 여부 플래그
default flag_run_election = False  # 선거 출마 플래그