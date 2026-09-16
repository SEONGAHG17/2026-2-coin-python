// 증감연산자
/*

값을 사용하는 시점이 중요하다!

++a
→ 먼저 증가
→ 증가한 값을 사용

a++
→ 먼저 사용
→ 그 다음 증가

*/



// 1.기본적인 증감연산자
public class Main {
    public static void main(String[] args) {

        int number = 10;

        number++;
        System.out.println(number);  // 11

        number--;
        System.out.println(number);  // 10
    }
}

// 2.전위증가와 후위증가
public class Main {
    public static void main(String[] args) {

        int a = 10;
        int b = ++a;

        System.out.println(a); // 11
        System.out.println(b); // 11


        int x = 10;
        int y = x++;

        System.out.println(x); // 11
        System.out.println(y); // 10
    }
}


// 전위 감소와 후위 감소
public class Main {
    public static void main(String[] args) {

        int a = 10;

        System.out.println(--a); // 9
        System.out.println(a);   // 9


        int b = 10;

        System.out.println(b--); // 10
        System.out.println(b);   // 9
    }
}

