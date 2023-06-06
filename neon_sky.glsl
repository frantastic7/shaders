vec3 palette(float t) {
    vec3 a = vec3(0.0, 0.2, 0.7);
    vec3 b = vec3(0.2, 0.3, 0.0);
    vec3 c = vec3(0.6, 1.0, 0.3);
    vec3 d = vec3(0.263, 0.16, 0.357);
    return a + b * sin(6.33 * (c * t + d));
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
    vec2 uv = (fragCoord * 2.0 - iResolution.xy) / iResolution.y;
    vec2 uv0 = uv;
    vec3 finalColor = vec3(0.0);

    for (float i = 0.0; i <  2.5; i++) {
        uv = fract(uv * 1.5) - 0.5;
        float d = length(uv) * exp(-length(uv0));
        vec3 col = palette(length(uv0) + i * 0.3 + iTime * 0.4);
        d = cos(d * 8.0  + iTime) / 8.0;
        d = abs(d);
        d = pow(0.01 / d, 1.2);
        d = d + sin(iTime * 3.5)/3.5;
        finalColor += col * d;
    }

    fragColor = vec4(finalColor, 1.0);
}