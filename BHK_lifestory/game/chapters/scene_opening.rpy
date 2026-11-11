label scene_opening:
    # ---------------------------------------------------------
    # 1. COLD OPEN: 강당 선거 단상 (시끄럽고 혼란스러운 현장)
    # ---------------------------------------------------------
    
    #play sound "audio/crowd_cheer.ogg" loop # 강당 웅성거림과 환호성
    window hide

    scene black with fade
    play music "audio/crowded.mp3" fadein 1.0
    $ renpy.pause(2.0)
    sys "다음은 기호 2번,{w=0.3} 김병연 후보의 연설이 있겠습니다!"
    $ renpy.pause(2.0)
    scene bg auditorium with fade   

    # 발걸음 소리
    play sound "audio/footsteps_stage.mp3" fadein 0.5
    sys "수백 개의 시선이 정면에서 꽂혀온다."
    stop sound fadeout 0.5
    sys "단상 위, 핀 조명 아래에 서서 마이크를 쥐었을 때——"
    stop music fadeout 0.5
    # ---------------------------------------------------------
    # 2. 정적과 내면 독백
    # ---------------------------------------------------------
    # 함성소리가 물속에 잠기듯 뚝 끊기거나 페이드아웃
    
    scene black with fade
    play music "bgm_mystery.mp3" fadein 1.0
    $ renpy.pause(1.0)
    
    sys "문득,{w=0.4} 아주 멍청한 생각이 스쳤다."
    sys "'내가 왜 인생을 걸고 이러고 있는 거지?'"

    $ renpy.pause(0.8)

    sys "인생이 언제부터 꼬이기 시작했는지는 명확하지 않다."
    sys "다만 분명한 것은, 밑바닥을 찍고 나서야 비로소 눈이 뜨였다는 사실이다."
    sys "이제부터 시작하는 이야기는 지금의 내가 되기까지의 이야기다."

    stop music fadeout 1.0
    # ---------------------------------------------------------
    # 3. 2002년 춘천 병실로 회귀
    # ---------------------------------------------------------
    $ renpy.pause(1.2)
    play music "audio/opening_theme.ogg" fadein 2.5

    scene bg hospital with fade
    window hide

    sys "2002년 9월 13일 춘천 모 병원 병실"

    $ renpy.pause(1.0)

    sys "부모님이 춘천 바닥에서 땀 흘려 일궈낸 작은 자영업의 터전 위에서,\n나는 지극히 평범하고 무탈하게 첫 울음을 터뜨렸다."
    sys "남부럽지 않았다. 어릴 적의 나는 먹고 싶은 건 먹었고, 떼쓰는 족족 손에 쥘 수 있었다."
    sys "적어도 그때까지는 몰랐다.\n내 인생이 낭떠러지 위를 걷는 곡예가 될 줄은."

    # 씬 정리 후 script.rpy의 다음 줄(scene_chapter_01)로 복귀
    $ renpy.pause(1.0)

    return