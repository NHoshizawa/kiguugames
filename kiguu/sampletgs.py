### インポート
import sys
import pygame
from pygame.locals import *
 
### 定数
SURFACE = Rect(0, 0, 640, 400) # 画面サイズ(X軸,Y軸,横,縦)
G_SIZE  = 100                  
G2_SIZE  = 150 				   # 画像サイズ
F_RATE  = 60                   # フレームレート
 
############################
### スプライトクラス継承 
############################
class MySprite(pygame.sprite.Sprite):
 
    ############################
    ### 初期化メソッド(ファイル名,X軸,Y軸,X軸移動,Y軸移動)
    ############################
    def __init__(self, name, x, y, mv_x, mv_y):
        pygame.sprite.Sprite.__init__(self)
 
        ### 透過変換でファイル読み込み
        self.image = pygame.image.load(name).convert_alpha()
 
        ### 画像サイズ変更
        self.image = pygame.transform.scale(self.image, (G_SIZE, G2_SIZE))
 
        ### 画像サイズ取得
        width  = self.image.get_width()
        height = self.image.get_height()
 
        ### 四角形オブジェクト生成
        self.rect = Rect(x, y, width, height)
 
        ### 移動位置設定
        self.mv_x = mv_x
        self.mv_y = mv_y
 
    ############################
    ### 画面更新
    ############################
    def update(self):
 
        ### 移動描写
        self.rect.move_ip(self.mv_x, self.mv_y)
 
        ### 画面の範囲外ならオブジェクト移動位置を反転
        if self.rect.left < 0 or self.rect.right  > SURFACE.width:
            self.mv_x = -self.mv_x
        if self.rect.top  < 0 or self.rect.bottom > SURFACE.height:
            self.mv_y = -self.mv_y
 
        ### 画面内に収める
        self.rect = self.rect.clamp(SURFACE)
    
    ############################
    ### オブジェクト描画
    ############################
    def draw(self, surface):
        surface.blit(self.image, self.rect)
 
############################
### メイン関数 
############################
def main():
 
    ### 画面初期化
    pygame.init()
    surface = pygame.display.set_mode(SURFACE.size)
 
    ### スプライトを作成
    img1 = MySprite("./"+"kiguu1/"+"c2"+".png",   0,   0, 8, 2)
    img2 = MySprite("./"+"kiguu1/"+"h2"+".png", 100, 100, 6, 4)
    img3 = MySprite("./"+"kiguu1/"+"s2"+".png", 200, 200, 4, 6)
    img4 = MySprite("./"+"kiguu1/"+"d2"+".png", 300, 300, 2, 8)
 
    ### グループ設定
    img_grp = pygame.sprite.Group(img1, img2, img3, img4)
 
    ### 時間オブジェクト生成
    clock = pygame.time.Clock()
 
    ### 無限ループ
    while True:
 
        ### フレームレート設定
        clock.tick(F_RATE)
 
        ### 背景色設定
        surface.fill((0,0,0))
 
        ### スプライトを更新
        img_grp.update()
 
        ### スプライトを描画
        img_grp.draw(surface)
 
        ### 画面更新
        pygame.display.update()
 
        ### イベント処理
        for event in pygame.event.get():
 
            ### 終了処理
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
 
############################
### 終了関数
############################
def exit():
    pygame.quit()
    sys.exit()
 
############################
### メイン関数呼び出し
############################
if __name__ == "__main__":
 
    ### 処理開始
    main()