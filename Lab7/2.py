import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Music Player")

songs = ["song1.mp3", "song2.mp3", "song3.mp3"]
music_files = ["Lab7\Music\song1.mp3", "Lab7\Music\song2.mp3", "Lab7\Music\song3.mp3"]
i = 0

font = pygame.font.Font(None, 32)

song_title = font.render(songs[i], True, (0, 0, 0))
pause_notice = font.render("PAUSED", True, (255, 0, 0))

pygame.mixer.music.load(music_files[i])
pygame.mixer.music.play()
pygame.mixer.music.set_endevent(pygame.USEREVENT)

x, y = pause_notice.get_rect().center

running = True
paused = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
            elif event.key == pygame.K_RIGHT:
                i = (i + 1) % len(music_files)
                pygame.mixer.music.load(music_files[i])
                pygame.mixer.music.play()
                song_title = font.render(songs[i], True, (0, 0, 0))
                pygame.mixer.music.set_endevent(pygame.USEREVENT)
            elif event.key == pygame.K_LEFT:
                i = (i - 1) % len(music_files)
                pygame.mixer.music.load(music_files[i])
                pygame.mixer.music.play()
                song_title = font.render(songs[i], True, (0, 0, 0))
                pygame.mixer.music.set_endevent(pygame.USEREVENT)
            elif event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.USEREVENT:
            i = (i + 1) % len(music_files)
            pygame.mixer.music.load(music_files[i])
            pygame.mixer.music.play()
            song_title = font.render(songs[i], True, (0, 0, 0))
            pygame.mixer.music.set_endevent(pygame.USEREVENT)

    screen.fill((255, 255, 255))

    screen.blit(song_title, (10, 10))

    if paused:
        screen.blit(pause_notice, (320 - x, 240 - y))

    pygame.display.update()
pygame.quit()