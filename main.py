def levelStart():
    if currentLevel == 1:
        tiles.set_current_tilemap(tilemap("""
            level1
        """))
        scene.set_background_color(0)
    elif currentLevel == 2:
        tiles.set_current_tilemap(tilemap("""
            level2
        """))
    elif currentLevel == 3:
        tiles.set_current_tilemap(tilemap("""
            level6
        """))
    elif currentLevel == 4:
        game.game_over(True)
        game.set_game_over_effect(True, effects.smiles)
    else:
        pass

def on_countdown_end():
    game.game_over(False)
    game.set_game_over_effect(False, effects.slash)
info.on_countdown_end(on_countdown_end)

def on_overlap_tile(sprite, location):
    global currentLevel
    currentLevel += 1
    levelStart()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_insignia,
    on_overlap_tile)

currentLevel = 0
player1 = sprites.create(img("""
        . . . . f f f f f . . . . . . . 
            . . . f e e e e e f . . . . . . 
            . . f d d d d e e e f . . . . . 
            . c d f d d f d e e f f . . . . 
            . c d f d d f d e e d d f . . . 
            c d e e d d d d e e b d c . . . 
            c d d d d c d d e e b d c . f f 
            c c c c c d d d e e f c . f e f 
            . f d d d d d e e f f . . f e f 
            . . f f f f f e e e e f . f e f 
            . . . . f e e e e e e e f f e f 
            . . . f e f f e f e e e e f f . 
            . . . f e f f e f e e e e f . . 
            . . . f d b f d b f f e f . . . 
            . . . f d d c d d b b d f . . . 
            . . . . f f f f f f f f f . . .
    """),
    SpriteKind.player)
player1.start_effect(effects.trail)
controller.move_sprite(player1)
scene.camera_follow_sprite(player1)
currentLevel = 1
levelStart()
info.start_countdown(10)