(* check pseudo equality of float values x and y *)
(* nearly_eq : ?threshold:float -> float -> float -> bool *)
let nearly_eq ?(threshold=1E-8) x y = abs_float (x -. y) < threshold

(* check whether all the elements in a bool list are true *)
(* all_true : bool list -> bool *)
let all_true = function
  | [] -> failwith "empty list"
  | _ as blist -> List.fold_left ( && ) true blist
