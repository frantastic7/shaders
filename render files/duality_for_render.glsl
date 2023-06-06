#version 330
uniform float iTime;
uniform vec2 iResolution;
out vec4 fragColor;

vec3 specter (float t) {
    vec3 a = vec3 (0.3,0.0,0.1);
    vec3 b = vec3 (0.1,0.9,0.0);
    vec3 c = vec3 (0.0,0.4,0.3);
    return a*b - sin (t) * (c*(c+t)-b);
}


void main() {
    vec2 uv = (gl_FragCoord.xy * 2.0 - iResolution) / min(iResolution.y, iResolution.x);
    vec2 uv0 = uv;
    vec3 finalColor = vec3(0.0);

    for (float i = 0.0; i < 4.5; i++) {
        uv = fract(uv * 1.5) - 0.5;
        float d = length(uv) * exp(-length(uv0));
        vec3 col = specter(length(uv0) + i * 0.3 + iTime * 0.4);
        d = abs(d)-sin(d * 4.5)/3.0;
        finalColor += col * d;
    }

    fragColor = vec4(finalColor, 1.0);
}
