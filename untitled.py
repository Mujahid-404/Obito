lane = 1[span_1](start_span)[span_1](end_span)
score = 0[span_2](start_span)[span_2](end_span)
speed = 6[span_3](start_span)[span_3](end_span)
boost = False[span_4](start_span)[span_4](end_span)

keys = pygame.key.get_pressed()[span_5](start_span)[span_5](end_span)

if keys[pygame.K_LEFT] and lane > 0:[span_6](start_span)[span_6](end_span)
    lane -= 1[span_7](start_span)[span_7](end_span)

if keys[pygame.K_RIGHT] and lane < 2:[span_8](start_span)[span_8](end_span)
    lane += 1[span_9](start_span)[span_9](end_span)

player.x = lanes[lane][span_10](start_span)[span_10](end_span)

for car in traffic:[span_11](start_span)[span_11](end_span)
    car.y += speed[span_12](start_span)[span_12](end_span)

if player.colliderect(boost_pad):[span_13](start_span)[span_13](end_span)
    boost = True[span_14](start_span)[span_14](end_span)
    speed = 9[span_15](start_span)[span_15](end_span)

score += int(speed)[span_16](start_span)[span_16](end_span)
