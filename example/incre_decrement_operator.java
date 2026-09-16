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


/*
int x = 5;
S.O.P(++x); // x에 1을 더한다 >> 출력한다. # print value) 6, X value) 6
	// x = x + 1
	// S.O.P(x)

int y = 9;
S.O.P(y++); // y 값을 먼저 출력하고 >> y = y+1 을 진행한다 # print value)5, Y value)6
S.O.P(y);	// 위 명령에서 y값이 6이 되었으므로, 출력하면 6!
	// S.O.P(y)
	// y = y + 1


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

