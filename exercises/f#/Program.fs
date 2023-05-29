// 2.1a

let vowelToUpper (c): string = 
    match c with
    | "a" -> "A"
    | "e" -> "E"
    | "i" -> "I"
    | "o" -> "O"
    | "u" -> "U"
    | _ -> c

let x = vowelToUpper "x"  
let a = vowelToUpper "a"

// 2.1b

// convert vowels to uppercase own implementation

let rec convertVowelsToUpper (str: string) : string =
    match str with
    | "" -> ""
    | _ ->
        let firstChar = str[0..0]
        let rest = str.[1..]
        let convertedChar = vowelToUpper firstChar
        let convertedRest = convertVowelsToUpper rest
        convertedChar + convertedRest

let picovina = convertVowelsToUpper "picovina"

// 2.2a

// list length own implementaion

let rec pmLength list =
    match list with
    | [] -> 0                     
    | _ :: tail -> 1 + pmLength tail 

let result = pmLength [1;2;3;4]

// 2.2b

let rec pclSum list = 
    match list with
    | [] -> 0
    | x :: tail -> x + pclSum tail

let result2 = pclSum [1;2;3;4]

// 2.3

// take specified part from list

let takeSome n ls = 
    match ls with
    | [] -> []
    | _ -> ls[0..n-1]

let result3 = takeSome 3 [1;2;3;4;5]

// 2.4a

// fold 
// own implementation

let rec pclFold func acc lst =
    match lst with
    | [] -> acc
    | x :: tail -> pclFold func (func acc x) tail

// 2.4b

let pclSumWithFold lst = pclFold (+) 0 lst

let result4 = pclSumWithFold [1;2;3;4;5]

// 2.5a

// fold back 
// own implementation

let rec pclFoldBack func acc lst =
    match lst with
    | [] -> acc
    | x :: tail -> func x (pclFoldBack func acc tail)

// 2.5b

let pclSumWithFoldBack lst =
    pclFoldBack (+) 0 lst

// 2.5c

// results can be different between pclFold and pclFoldBack in non-associative scenarios like subtraction

let result5 = pclFold (-) 0 [1;2;3]
let result6 = pclFoldBack (-) 0 [1;2;3]

// 2.6

// increment int list

let rec pclIncList lst =
    match lst with
    | [] -> []
    | x :: tail -> (x + 1) :: pclIncList tail

let result7 = pclIncList [1;2;3;4]

// 2.7a

// map
// own implementation

let rec pclMap fn lst =
    match lst with
    | [] -> []
    | x :: tail -> fn x :: pclMap fn tail

// 2.7b

let pclIncListWithMap lst = pclMap (fun x -> x + 1) lst

let result8 = pclIncListWithMap [1;2;3;4;5]

// 2.8a

// filter
// own implementation

let rec pclFilter predicate lst =
    match lst with
    | [] -> []
    | x :: tail -> if (predicate x) then x :: pclFilter predicate tail else pclFilter predicate tail


// 2.8b

let rec pclEven x = x % 2 = 0

// 2.8c

let result9 = pclFilter pclEven [1;2;3;4;5;6;7;8;9;10]

// for some reason there are 2 sets
// of exercises that start with number 2 (i.e. 2.1)
// but the set that comes later in the exercise list i have given
// has been skipped here because they are super simple

// 3.1

// count vowels
// fold
// tuples
// seq.tolist

let countVowel vowelCount vowel = 
    let (a, e, i, o, u) = vowelCount
    match vowel with
        | 'a' | 'A'-> (a + 1, e, i, o, u)
        | 'e' | 'E' -> (a, e + 1, i, o, u)
        | 'i' | 'I' -> (a, e, i + 1, o, u)
        | 'o' | 'O' -> (a, e, i, o + 1, u)
        | 'u' | 'U' -> (a, e, i, o, u + 1)
        | _ -> vowelCount

let countNumOfVowels str = List.fold countVowel (0, 0, 0, 0, 0) (Seq.toList str)

let result10 = countNumOfVowels "Higher-order functions can take and return functions of any order"

// 3.2

// is prime
// primes up to
// primesupto

let isPrime n =
    let rec isDivisibleBy k d =
        if d * d > k then
            true
        elif k % d = 0 then
            false
        else
            isDivisibleBy k (d + 1)
    n > 1 && isDivisibleBy n 2

let primesUpTo n =
    let lst = [2..n]
    List.filter isPrime lst

let result11 = primesUpTo 10

// 3.3

// recursion 
// fibonacci

let rec pclFib n =
    match n with
    | 0 -> 0
    | 1 -> 1
    | _ -> pclFib (n - 1) + pclFib (n - 2)

let result12 = pclFib 8


// 3.4a

let doubleNum x = x * 2

let sqrNum x = x * x

// 3.4b

let pclQuad x = doubleNum(doubleNum x)

// 3.4c

let pclFourth x = sqrNum(sqrNum x)

// 4.1 & 5.1

// shape area
// union
// type
// object

type Shape = | Rectangle | Triangle

type PclShape = { shape: Shape; a: float; b: float }

let pclArea x = if (x.shape = Rectangle) then x.a * x.b  else ((x.a * x.b)/2.0) 
let pclPerimeter x = if (x.shape = Rectangle) then x.a*2.0 + x.b*2.0 else x.a*2.0 + x.b 
    
let rect: PclShape = { 
    shape = Rectangle
    a = 4
    b = 3
}

let triangle: PclShape = {
    shape = Triangle
    a = 5
    b = 2137
}

let rectangleArea = pclArea rect
let triangleArea = pclArea triangle
let rectanglePerimeter = pclPerimeter rect
let trianglePerimeter = pclPerimeter triangle

// 5.2

// tail recursion 
// fibonacci

let fibonacci n =
    let rec fibonacciTail n acc b =
        match n with
        | 0 -> acc
        | _ -> fibonacciTail (n - 1) b (acc + b)
    fibonacciTail n 0 1

let result13 = fibonacci 8

// 5.3

// factorial 
// continuation

let rec factorial n cont =
    match n with
    | 0 -> cont 1
    | _ -> factorial (n - 1) (fun x -> cont (n * x))

let printFactorial result = printfn "Factorial %d" result

factorial 5 printFactorial

// 6a

// integer tree
// discriminated unions
// tuple types

type IntegerTree =
    | Leaf of int
    | Node of IntegerTree * IntegerTree

let rec sumIntegerTree tree =
    match tree with
    | Leaf value -> value
    | Node (left, right) -> sumIntegerTree left + sumIntegerTree right

let tree1 = Node (Leaf 1, Node (Leaf 2, Leaf 3))
let result15 = sumIntegerTree tree1  // Result: 6

let tree2 = Node (Leaf 4, Node (Leaf 5, Leaf 6))
let result16 = sumIntegerTree tree2  // Result: 15

// 6b

// word letter count

type WordLetterCount =
    { WordCount : int
      LetterCount : int }

let countWordnLetter (str: string) =
    let wordCount = str.Split [| ' ' |]
    let letterCount = wordCount |> Array.sumBy (fun w -> w.Length)
    { WordCount = wordCount.Length; LetterCount = letterCount }

// 7

// leap year
// days to end year
// if else

let isLeapYear year =
    year % 4 = 0 && (year % 100 <> 0 || year % 400 = 0)

let addDays result year = if isLeapYear year then result+366 else result+365

let daysToEndYear year = List.fold addDays 0 [1 .. year]

let result17 = daysToEndYear 1




