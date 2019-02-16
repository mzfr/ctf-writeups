# Login

__PROBLEM__

We found this file and could not make a sense out of it. One of our lead analyst stated that it could contains a user name and password in it. Can you help us identify it?

Note: Add xiomara{} tags before submitting the flag. And her flag is in the form xiomara{Username:Password}

[File](Login)

__SOLUTION__

We are provided with a `Java class` file.
Using [this](http://www.javadecompilers.com/result) website we decompile the class file and get the following code
```java
import java.util.Scanner;

public class Login {
  public Login() {}

  public static void main(String[] paramArrayOfString) { Scanner localScanner = new Scanner(System.in);



    String str1 = "55534552";

    String str2 = "54455354";


    StringBuilder localStringBuilder = new StringBuilder("");


    for (int i = 0; i < str1.length(); i += 2) {
      str6 = str1.substring(i, i + 2);
      localStringBuilder.append((char)Integer.parseInt(str6, 16));
    }
    String str3 = localStringBuilder.toString();


    localStringBuilder = new StringBuilder("");
    for (i = 0; i < str2.length(); i += 2) {
      str6 = str2.substring(i, i + 2);
      localStringBuilder.append((char)Integer.parseInt(str6, 16));
    }

    String str4 = localStringBuilder.toString();


    System.out.print("Enter Username ");
    String str5 = localScanner.nextLine();
    System.out.print("Enter Password ");
    String str6 = localScanner.nextLine();

    if ((str5.equals(str3)) && (str6.equals(str4))) {
      System.out.print("Login Succesful...");
    } else {
      System.out.print("Login Failed.");
    }
  }
}
```

we can see that there's lot of stuff happening but in the end there's a comparision between `str5`(username input) and `str3` and `str6`(password input) and `str4`. So without thinking much we simply print those(str3 & str4) value. Now the code becomes

```java
import java.util.Scanner;

public class Login {
    public Login() {}
  public static void main(String[] paramArrayOfString) {
    Scanner localScanner = new Scanner(System.in);
    String str1 = "55534552";
    String str2 = "54455354";
    String str6 = "";
    int i;
    StringBuilder localStringBuilder = new StringBuilder("");


    for (i = 0; i < str1.length(); i += 2) {
      str6 = str1.substring(i, i + 2);
      localStringBuilder.append((char)Integer.parseInt(str6, 16));
    }
    String str3 = localStringBuilder.toString();


    localStringBuilder = new StringBuilder("");
    for (i = 0; i < str2.length(); i += 2) {
      str6 = str2.substring(i, i + 2);
      localStringBuilder.append((char)Integer.parseInt(str6, 16));
    }

    String str4 = localStringBuilder.toString();


    System.out.print("Enter Username ");
    String str5 = localScanner.nextLine();
    System.out.print("Enter Password ");
    str6 = localScanner.nextLine();
    System.out.println("Username is: "+str3+"password is: "+str4);

    if ((str5.equals(str3)) && (str6.equals(str4))) {
      System.out.print("Login Succesful...");
    } else {
      System.out.print("Login Failed.");
    }
}
}
```

Compile and run the file and we'll get the output

FLAG - xiomara{USER:TEST}
