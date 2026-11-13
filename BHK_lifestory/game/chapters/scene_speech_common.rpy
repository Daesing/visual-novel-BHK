# ==============================================================================
# scene_speech_common.rpy : 오프닝/엔딩에서 공유하는 강당 연설 연출
# ==============================================================================

# 강당 사회자 호명 (암전 + 함성)
label speech_announce:
    scene black with fade
    play music "audio/crowded.ogg" fadein 1.0
    $ renpy.pause(2.0)
    sys "다음은 기호 2번,{w=0.3} 김병연 후보의 연설이 있겠습니다!"
    $ renpy.pause(2.0)
    return

# 단상에 올라 마이크를 쥐는 장면
label speech_stage(last_line="단상 위, 핀 조명 아래에 서서 마이크를 쥐었을 때——"):
    scene bg auditorium with fade

    # 발걸음 소리
    play sound "audio/footsteps_stage.ogg" fadein 0.5
    sys "수백 개의 시선이 정면에서 꽂혀온다."
    stop sound fadeout 0.5
    sys "[last_line]"
    stop music fadeout 0.5
    return

# 정적과 내면 독백 (함성소리가 물속에 잠기듯 끊김)
label speech_doubt:
    scene black with fade
    play music "audio/bgm_mystery.ogg" fadein 1.0
    $ renpy.pause(1.0)

    sys "문득,{w=0.4} 아주 멍청한 생각이 스쳤다."
    sys "'내가 왜 인생을 걸고 이러고 있는 거지?'"
    return
