class MathUtil {
    static square(x) {
        return x * x;
    }
    static cube(x) {
        return x * x * x;
    }
}
document.addEventListener("DOMContentLoaded",function() {
    document.getElementById("classStaticMethodsOutput").innerHTML =
    `Sqare of 4:${MathUtil.square(4)}
    Cube of 3:${MathUtil.cube(3)}`;
});