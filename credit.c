//#include <cs50.h>
#include <stdio.h>
#include <stdbool.h>

bool amex(long z);
bool mastercard(long z);
bool visa(long z);
bool luhn(long z);

int d1=0,  d2=0,  d3=0,  d4=0, 
    d5=0,  d6=0,  d7=0,  d8=0, 
    d9=0, d10=0, d11=0, d12=0,
    d13=0, d14=0, d15=0, d16=0;
 
int main(void)
{
// get card number with 13, 15, or 16 digits
    long z;
    do
    {
        z = 4003600000000014 ; //get_long("Credit Card number? ");
    }
    while (z < 1000000000000 || z > 9999999999999999 || (z < 100000000000000 && z > 9999999999999));
    d1  = z % 10;
    d2  = z/10 % 10;
    d3  = z/100 % 10;
    d4  = z/1000 % 10;
    d5  = z/10000 % 10;
    d6  = z/100000 % 10;
    d7  = z/1000000 % 10;
    d8  = z/10000000 % 10;
    d9  = z/100000000 % 10;
    d10 = z/1000000000 % 10;
    d11 = z/10000000000 % 10;
    d12 = z/100000000000 % 10;
    d13 = z/1000000000000 % 10;
    d14 = z/10000000000000 % 10;
    d15 = z/100000000000000 % 10;
    d16 = z/1000000000000000 % 10;
   


// Is it an Amex?
bool amex(long z);
    if (z > 999999999999999 || z < 100000000000000)
    {
        return false;
    }
    if (o != 3)
    {
        return false;
    }
    if (n != 4 && n != 7)
    {
        return false;
    }
    if (bool luhn(z) == true)
    {
        return true;
        printf("AMEX\n");
    }
    else
    {
        return false;
    }




// Is it a Mastercard?
bool mastercard(long z);

    if (z > 9999999999999999 || z < 1000000000000000)
    {
        return false;
    }
    if (p != 5)
    {
        return false;
    }
    if (o != 1 && o != 2 && o != 3 && o != 4 && o != 5)
    {
        return false;
    }
    if (bool luhn(z) == true)
    {
        return true;
        printf("MASTERCARD\n");
    }
    else
    {
        return false;
    }




// Is it a Visa?
bool visa(long z);

    if (z > 9999999999999999 || z < 1000000000000 || (z > 9999999999999 && z < 1000000000000000))
    {
        return false;
    }

        // 13 digit case
        if (z <= 9999999999999 && z >= 1000000000000)
        {
            if (m != 4)
            {
                return false;
            }
            if (bool luhn(z) == true)
            {
                return true;
                printf("VISA\n");
            }
            else
            {
                return false;
            }
        }

        // 16 digit case
        if (z <= 9999999999999999 && z >= 1000000000000000)
        {
            if (p != 4)
            {
                return false;
            }
            if (bool luhn(z) == true)
            {
                return true;
                printf("VISA\n");
            }
            else
            {
                return false;
            }
        }



    // check if invalid card result (i.e. not amex or mastercard or visa)

    if(bool amex == false && bool mastercard == false && bool visa == false)
    printf("INVALID\n");



bool luhn(z);

// if Amex (i.e. 15 digits)
if (z > 999999999999999 || z < 100000000000000)
{
    // starting with second to last digit, multiply every other digit by 2
    int la = (b*2)%10 + (b*2)%100 + (d*2)%10 + (d*2)%100 + (f*2)%10 + (f*2)%100 + (h*2)%10 + (h*2)%100 + (j*2)%10 + (j*2)%100 + (l*2)%10 + (l*2)%100 + (n*2)%10 + (n*2)%100;

    int lb = a + c + e + g + i + k + m + o;

    int lc = la + lb;

    if (lc % 10 = 0)
        {
            bool luhn = true;
        }
}

// if Mastercard or 16-digit Visa (i.e. 16 digits)
if (z > 9999999999999999 || z < 1000000000000000)
{
    int la = (b*2)%10 + (b*2)%100 + (d*2)%10 + (d*2)%100 + (f*2)%10 + (f*2)%100 + (h*2)%10 + (h*2)%100 + (j*2)%10 + (j*2)%100 + (l*2)%10 + (l*2)%100 + (n*2)%10 + (n*2)%100 + (p*2)%10 + (p*2)%100;

    int lb = a + c + e + g + i + k + m + o;

    int lc = la + lb;

    if (lc % 10 = 0)
        {
            bool luhn = true;
        }
}

// if 13-digit Visa (i.e. 13 digits)
if (z <= 9999999999999 && z >= 1000000000000)
{
    int la = (b*2)%10 + (b*2)%100 + (d*2)%10 + (d*2)%100 + (f*2)%10 + (f*2)%100 + (h*2)%10 + (h*2)%100 + (j*2)%10 + (j*2)%100 + (l*2)%10 + (l*2)%100;

    int lb = a + c + e + g + i + k + m;

    int lc = la + lb;

    if (lc % 10 = 0)
        {
            bool luhn = true;
        }
}
}
