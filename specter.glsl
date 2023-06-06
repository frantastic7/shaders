vec3 palette(float t) {
    vec3 a = vec3 (0.0, 0.1, 0.3);
    vec3 b = vec3 (0.0, 0.5, 0.0);
    vec3 c = vec3 (0.2, 0.7, 0.5);
    vec3 d = vec3 (0.5, 0.0, 0.5);
    return a * b + cos (3.14* c*t + d);
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
    vec2 uv = (fragCoord * 2.0 - iResolution.xy) / iResolution.y;
    vec2 uv0 = uv;
    vec3 finalColor = vec3(0.0);

    for (float i = 0.0; i < 2.0; i++) {
        uv = fract(uv * 1.5) - 0.5;
        float d = length(uv) * exp(-length(uv0));

        vec3 col = palette(length(uv0) + i * 0.7 + iTime * 0.5);
        for (float j = 0.0 ; j < 1.0 ; j++)
            {
            d = sin(d * 6.0  + iTime) / 6.0;
            d = abs(d);
            d = pow(0.03 / d, 1.2);
            d = d + cos(iTime * 2.5)/3.5;
            }

        finalColor += col * d;
    }

    fragColor = vec4(finalColor, 1.0);
}