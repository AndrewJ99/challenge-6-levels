function levelStart () {
    if (currentLevel == 1) {
        tiles.setCurrentTilemap(tilemap`level1`)
        scene.setBackgroundColor(0)
    } else if (currentLevel == 2) {
        tiles.setCurrentTilemap(tilemap`level2`)
    } else if (currentLevel == 3) {
        tiles.setCurrentTilemap(tilemap`level2`)
    } else {
    	
    }
}
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.collectibleInsignia, function (sprite, location) {
    currentLevel += 1
})
let currentLevel = 0
let player1 = sprites.create(img`
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
    `, SpriteKind.Player)
player1.startEffect(effects.trail)
controller.moveSprite(player1)
scene.cameraFollowSprite(player1)
currentLevel = 1
levelStart()
