label scene_final:
    
    window hide

    scene black with fade
    play music "audio/crowded.mp3" fadein 1.0
    $ renpy.pause(2.0)
    sys "다음은 기호 2번,{w=0.3} 김병연 후보의 연설이 있겠습니다!"
    $ renpy.pause(2.0)
    window hide

    # ---------------------------------------------------------
    # 2. 정적과 내면 독백
    # ---------------------------------------------------------
    # 함성소리가 물속에 잠기듯 뚝 끊기거나 페이드아웃
    
    scene black with fade
    play music "bgm_mystery.mp3" fadein 1.0
    $ renpy.pause(1.0)
    
    sys "문득,{w=0.4} 아주 멍청한 생각이 스쳤다."
    sys "'내가 왜 인생을 걸고 이러고 있는 거지?'"
    scene bg auditorium with fade   

    # 발걸음 소리
    play sound "audio/footsteps_stage.mp3" fadein 0.5
    sys "수백 개의 시선이 정면에서 꽂혀온다."
    stop sound fadeout 0.5
    sys "단상 위, 핀 조명 아래에 서서 마이크를 쥐었을 때"
    stop music fadeout 0.5