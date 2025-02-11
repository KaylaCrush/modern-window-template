#version 430

out vec4 fragColor;

uniform vec2 resolution;
uniform float time;

void main(){
    vec3 col = vec3(0.0);
    fragColor = vec4(col,1.0);
}
