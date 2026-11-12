# ==============================================================================
# script.rpy : 메인 진입점 및 챕터 라우터
# ==============================================================================

label start:
    # 0. 초기 환경 세팅
    stop music fadeout 1.0
    scene black with fade

    # 1. 오프닝
    call scene_opening

    # 2. 1장: 삼육초와 중학교의 방황
    call scene_chapter_01

    # 3. 2장: 고교 진학, 멘헤라 연애, 나락
    #call scene_chapter_02

    # 4. 3장: 각성과 스펙 빌드업
    #call scene_chapter_03

    # 5. 4장: 전교회장 선거전 (분기 시작)
    call scene_chapter_04

    return