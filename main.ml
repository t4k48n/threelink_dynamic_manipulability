(* 把持物体の質量の不確かさについてのシミュレーションをする *)

open Model

let generate_dynamic_manipulabilities fname qlist zlist =
  let dynamic_manipulabilities =
    Array.map (fun q -> Array.map (fun z -> dynamic_manipulability q z) zlist) qlist in
  let ch = open_out fname in
  let fprint_line d =
    let sep = ref "" in
    Array.iter (fun e -> Printf.fprintf ch "%s%f" !sep e; sep := ",") d;
    Printf.fprintf ch "\n" in
  Array.iter fprint_line dynamic_manipulabilities;
  close_out ch

let generate_postures fname qlist =
  let ch = open_out fname in
  let fprint_angle (Angle (q1, q2, q3)) =
    Printf.fprintf ch "%f,%f,%f\n" q1 q2 q3 in
  Array.iter fprint_angle qlist;
  close_out ch

let () =
  (* 円周率 *)
  let pi = 4.0 *. atan 1.0 in
  (* 乱数シードを現在時刻に従い初期化 *)
  Random.init @@ int_of_float @@ Unix.gettimeofday () *. 1E9;
  (* MC法の粒子数 *)
  let unum = 15000 in
  (* 把持物体の質量についての不確かさを生成 *)
  let uncertainties =
    Array.init
      unum
      (fun _ ->
        let u = Utils.uniform (-1.) 1. in
        Unc (0., 0., 0., 0., 0., 0., 0., 0., 0., u)) in
  let postures =
    (* 角度のtick数 *)
    let tnum = 73 in
    let ticks = Utils.list_linspace 0. (2. *. pi) tnum in
    let ps = List.map (fun q2 -> List.map (fun q3 -> Angle (0., q2, q3)) ticks) ticks in
    Array.of_list @@ List.concat ps in
  let dynamic_manipulability_fname = "dynamic_manipulabilities.csv" in
  if not (Sys.file_exists dynamic_manipulability_fname) then begin
      generate_dynamic_manipulabilities
        dynamic_manipulability_fname
        postures
        uncertainties
    end;
  let posture_fname = "postures.csv" in
  if not (Sys.file_exists posture_fname) then begin
      generate_postures
        posture_fname
        postures
    end
