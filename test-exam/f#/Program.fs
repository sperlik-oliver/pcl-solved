﻿// 1a

// square root of first element

 let sqrOnlyFirst ls =
    match ls with
        | hd :: _ -> hd * hd

let result1 = sqrOnlyFirst [2;4;6] // 4
let result2 = sqrOnlyFirst [] // error


 let sqrOnlyFirstFixed ls =
    match ls with
      | [] -> 0 // needed to not error with empty list
      | hd :: _ -> hd * hd

let result3 = sqrOnlyFirstFixed [2;4;6]
let result4 = sqrOnlyFirstFixed []

// 1b

// string to list

let rec stringToList str =
    match str with
    | "" -> []
    | _ -> 
        let firstChar = str.[0]
        firstChar :: stringToList str[1..]

let result5 = stringToList "Jebem Boha"


// 2a

// record type
// vector
// add vector
// calculate vector length

type Vector = {
    a: int;
    b: int;
    c: int;
    d: int;
    e: int;
}

// 2b

let vecLen vector = vector.a + vector.b + ( vector.c) + vector.d + vector.e

// 2c

let vecAdd vectorA vectorB = vecLen vectorA + vecLen vectorB


// 3a

// repeat string
// duplicate string

let rec rerun s n =
    match s, n with
    | _, 0 -> ""
    | _, _ -> s + rerun s (n-1)


let result6 = rerun "pica" 3


// 3b

// repeat string
// tail recursion


let rec rt s n acc = 
    match s, n with
    | _, 0 -> acc
    | _, _ -> rt s (n-1) (s+acc)

let rerunTail s n = rt s n ""

let result7 = rerunTail "kokot" 3

// 4

// sequences
// loops

let f1 i j k =
    seq {
         for x in [0 .. i] do
             for y in [0 .. j] do 
                if x+y < k then yield (x,y)
}
let f2 f p sq =
    seq {
         for x in sq do
            if p x then yield f x
}
let f3 g sq =
    seq {
         for s in sq do
            yield! g s
}

// 4a

let result8 = List.ofSeq(f1 2 2 3) // [(0, 0); (0, 1); (0, 2); (1, 0); (1, 1); (2, 0)]

// 4b
// wtf is happening here i have no idea
let f2seq f p sq =
    sq
    |> Seq.filter p
    |> Seq.map f

// 5a

// discriminated union
// tuples
// expr
// expression
// to string
// print
// recursion

type expr = | Const of int
            | BinOpr of expr * string * expr

let expr1 = Const(1)
let expr2 = BinOpr(Const(1), "+", BinOpr(Const(1), "+", Const(2)))
let expr3 = BinOpr(Const(3), "-", Const(2))

// 5b

let rec toString expr =
        match expr with
        | Const x -> string x
        | BinOpr (x, op, y) -> sprintf "(%s %s %s)" (toString x) op (toString y)

let result10 = toString expr2

// 6

// record type
// mailbox processor

type Product = {
    name: string;
    quantity: int;
}

let mailbox: MailboxProcessor<Product> =
    MailboxProcessor.Start(fun inbox ->
        let rec loop =
            async {
                let! order = inbox.Receive()

                printfn "%s %d" order.name order.quantity 
                printfn "\n"
                return! loop
            }

        loop)

let order1 = mailbox.Post({ 
    name = "Picovina" 
    quantity = 69420
    })



















