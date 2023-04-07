//#include <cs50.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool amex(long z);
bool mastercard(long z);
bool visa(long z);
bool luhn(long z);
int check_cc_number(long z);

int d1=0,  d2=0,  d3=0,  d4=0, 
    d5=0,  d6=0,  d7=0,  d8=0, 
    d9=0, d10=0, d11=0, d12=0,
    d13=0, d14=0, d15=0, d16=0;
/*
Standard Test Cards
American Express	378282246310005
American Express	371449635398431
American Express Corporate	378734493671000
Mastercard	2221000000000009
Mastercard	2223000048400011
Mastercard	2223016768739313
Mastercard	5555555555554444
Mastercard	5105105105105100
Mastercard	5199999999999991 
Mastercard  5299999999999990
Visa	4111111111111111
Visa	4012888888881881
Visa	4222222222222
Visa	4999991111111113
Visa    4999992222222229
*/

int main(void)
{
// get card number with 13, 15, or 16 digits
    long z;
    int error_code;
    z = 4003600000000014 ; error_code = check_cc_number(z); if (error_code != 0) printf("error code %d \n", error_code);
    z = 6176292929       ; error_code = check_cc_number(z); if (error_code != 0)printf("error code %d \n", error_code);
    // paypal test examples
    // amex
    z = 378282246310005 ; error_code = check_cc_number(z); if (error_code != 0)printf("error code %d \n", error_code);
    z = 371449635398431 ; error_code = check_cc_number(z); if (error_code != 0)printf("error code %d \n", error_code);
    z = 378734493671000 ; error_code = check_cc_number(z); if (error_code != 0)printf("error code %d \n", error_code);
    // mastercard
    z = 2221000000000009 ; error_code = check_cc_number(z); if (error_code != 0)printf("error code %d \n", error_code);
    z = 2223000048400011 ; error_code = check_cc_number(z); if (error_code != 0)printf("error code %d \n", error_code);
    z = 2223016768739313 ; error_code = check_cc_number(z); if (error_code != 0)printf("error code %d \n", error_code);
    z = 5555555555554444 ; error_code = check_cc_number(z); if (error_code != 0)printf("error code %d \n", error_code);
    z = 5105105105105100 ; error_code = check_cc_number(z); if (error_code != 0)printf("error code %d \n", error_code);
    z = 5199999999999991 ; error_code = check_cc_number(z); if (error_code != 0)printf("error code %d \n", error_code);
    z = 5299999999999990 ; error_code = check_cc_number(z); if (error_code != 0)printf("error code %d \n", error_code);
    // visa
    z = 4111111111111111 ; error_code = check_cc_number(z); if (error_code != 0)printf("error code %d \n", error_code);
    z = 4012888888881881 ; error_code = check_cc_number(z); if (error_code != 0)printf("error code %d \n", error_code);
    z = 4222222222222 ; error_code = check_cc_number(z); if (error_code != 0)printf("error code %d \n", error_code);
    z = 4999991111111113 ; error_code = check_cc_number(z); if (error_code != 0)printf("error code %d \n", error_code);
    z = 4999992222222229 ; error_code = check_cc_number(z); if (error_code != 0)printf("error code %d \n", error_code);     
}

//
// check credit card number
//
int check_cc_number(long z){
    printf("checking %ld : ", z);
    if  (z < 1000000000000 || z > 9999999999999999)
        {
            //
            // less than 13 and more than 16 digits INVALID
            //
            printf("INVALID\n");
            return (1);            
        }
    else
    {
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
        if (luhn(z)) {
            if (visa(z)){
                printf("VISA\n");
                return (0);                        
            }
            else if (amex(z)) {
                printf("AMEX\n");
                return (0);                        
            } else if (mastercard(z)) {
                printf("MASTERCARD\n");
                return (0);                        
            } else {
                //
                // neither ...
                //
                printf("INVALID\n");
                return(3);                       
            }
        } else {
            //
            // failed the checksum validation luhn
            //
            printf("INVALID\n");
            return(2);                        
        }
         
    } 
}

//  
//  for luhn algo checksum:
//  calculate the sum of the digits of the 
//  digit multiplied by 2
//
int double_and_sum (int digit){
    int twice = digit * 2;
    return ( twice / 10 + twice % 10 );
}

//
//  luhn algo is universal, 
//  leading zeroes don't effect the results in case of 13 or 15 digits
//  Multiply every other digit by 2, starting with the number’s second-to-last digit, 
//  and then add those products’ digits together. (odd digits)
//  Add the sum to the sum of the digits that weren’t multiplied by 2. (even digits)
//  If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), 
//  the number is valid!
//
bool luhn(long z){
    int odd_digits_sum = d1+d3+d5+d7+d9+d11+d13+d15 ;
    int even_digits_sum = double_and_sum (d2) + double_and_sum (d4) + double_and_sum (d6) +
                      double_and_sum (d8) + double_and_sum (d10) + double_and_sum (d12) +
                      double_and_sum (d14) + double_and_sum (d16) ;
    return ( ((even_digits_sum + odd_digits_sum) % 10) == 0 );
}

//
//  Is it an Amex?
//  American Express uses 15-digit numbers
//  All American Express numbers start with 34 or 37
//
bool amex(long z) {
    if (d16  > 0 ||      //more than 15 digits
        d15 != 3 ||      //doesn't start with 3
        ( d14  != 4 && d14 != 7 )   // neither 34 nor 37 
        ) {
        return false;
    } else {
        return true;
    }
}
  
//
//  Is it a Mastercard?
//  MasterCard uses 16-digit numbers
//  MasterCard numbers start with 51, 52, 53, 54, or 55
//
bool mastercard(long z){
    if ( d16 != 5 ||      //doesn't start with 5
         ( d15  < 1 || d15 > 5 )   // not between 51 and 55
       ) {
        return false;
    } else {
        return true;
    }
}

//
//  Is it a Visa?
//  Visa uses 13- and 16-digit numbers.
//  All Visa numbers start with 4
//
bool visa(long z) {
    if (d16 == 4 ||     // 16 digit numbers
       (d13 == 4 && (d16+d15+d14) == 0) // 13 digit case
       ) 
    {
        return true;
    } else {
        return false;
    }
}
