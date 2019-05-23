(* check pseudo equality of float values x and y *)
(* nearly_eq : ?threshold:float -> float -> float -> bool *)
let nearly_eq ?(threshold=1E-8) x y = abs_float (x -. y) < threshold

(* check whether all the elements in a bool list are true *)
(* all_true : bool list -> bool *)
let all_true = function
  | [] -> failwith "empty list"
  | _ as blist -> List.fold_left ( && ) true blist

(* sample a value from uniform distribution U(a, b) *)
(* uniform : float -> float -> float *)
let uniform a b =
  if a > b then failwith "a > b";
  Random.float (b -. a) +. a

(* Generate an array [|a; a+.d; a+.d+.d; ...; b|].
 * The length of the array is n. As the example, a and b are included. *)
let array_linspace a b n =
  if a > b then failwith "a > b";
  match n with
    | 0 -> [||]
    | 1 -> [|a|]
    | _ as n -> begin
        let d = (b -. a) /. (float @@ n - 1) in
        Array.init n (fun i -> a +. float i *. d)
      end

(* Generate an list [|a; a+.d; a+.d+.d; ...; b|].
 * The length of the list is n. As the example, a and b are included. *)
let list_linspace a b n =
  if a > b then failwith "a > b";
  match n with
    | 0 -> []
    | 1 -> [a]
    | _ as n -> begin
        let d = (b -. a) /. (float @@ n - 1) in
        List.init n (fun i -> a +. float i *. d)
      end
