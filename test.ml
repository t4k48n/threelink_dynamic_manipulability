open Utils

let nearly_eq_tests =
  let t1 = nearly_eq 0.33333333333333333333 (1. /. 3.) = true in
  let t2 = nearly_eq ~threshold:1E0 0.1 0.2 = true in
  let t3 = nearly_eq ~threshold:1E-6 0.11111 0.11112 = false in
  [t1; t2; t3]

let all_true_tests =
  let t1 = all_true [true; true; true] = true in
  let t2 = all_true [false] = false in
  let t3 = try (ignore (all_true []); false) with | _ -> true in
  [t1; t2; t3]

let uniform_tests =
  let samples = Array.init 100000 (fun _ -> uniform 0. 1.) in
  let t1 =
    let is_in = Array.map (fun s -> 0. <= s && s <= 1.) samples in
    Utils.all_true (Array.to_list is_in) in
  let t2 =
    let total = Array.fold_left ( +. ) 0. samples in
    Utils.nearly_eq ~threshold:(1.0 *. 0.02) (total /. float (Array.length samples)) 0.5 in
  [t1; t2]

let array_linspace_test =
  let t1 =
    Utils.all_true
      @@ Array.to_list
        @@ Array.map2 Utils.nearly_eq (array_linspace 0. 1. 3) [|0.; 0.5; 1.|] in
  let t2 =
    Utils.all_true
      @@ Array.to_list
        @@ Array.map2 Utils.nearly_eq (array_linspace 0. 1. 1) [|0.|] in
  let t3 =
    (array_linspace 0. 1. 0) = [||] in
  [t1; t2; t3]

let list_linspace_test =
  let t1 =
    Utils.all_true
      @@ List.map2 Utils.nearly_eq (list_linspace 0. 1. 3) [0.; 0.5; 1.] in
  let t2 =
    Utils.all_true
      @@ List.map2 Utils.nearly_eq (list_linspace 0. 1. 1) [0.] in
  let t3 =
    (list_linspace 0. 1. 0) = [] in
  [t1; t2; t3]

open Model

let eq_point_tests =
  let t1 =
    eq_point (Point (1., 2.)) (Point (1., 2.)) = true in
  let t2 =
    eq_point (Point (1.000000000000001, 2.)) (Point (1., 2.)) = true in
  let t3 =
    eq_point ~threshold:1E-20 (Point (1.0000001, 2.)) (Point (1., 2.)) = false in
  let t4 =
    eq_point (Point (-1., 2.)) (Point (1., -2.)) = false in
  [t1; t2; t3; t4]

let eq_mat_tests =
  let t1 =
    eq_mat
        (M22 (1., 2., 3., 4.))
        (M22 (1., 2., 3., 4.))
      = true in
  let t2 =
    eq_mat
        (M23 (1., 2., 3., 4., 5., 6.))
        (M23 (0., 2., 3., 4., 5., 6.))
      = false in
  [t1; t2]

let det_mat_tests =
  let t1 =
    let m = M22 (1., 0., 0., 1.) in
    det_mat m = 1. in
  let t2 =
    let m = M22 (0., 0., 0., 1.) in
    det_mat m = 0. in
  [t1; t2]

let trans_mat_tests =
  let t1 =
    eq_mat
      (trans_mat (M22 (1., 3., 2., 4.)))
      (M22 (1., 2., 3., 4.)) in
  let t2 =
    eq_mat
      (trans_mat (M23 (1., 2., 3., 4., 5., 6.)))
      (M32 (1., 4., 2., 5., 3., 6.)) in
  [t1; t2]

let inv_mat_tests =
  let t1 =
    inv_mat (M33 (1., 0., 0., 0., 1., 0., 0., 0., 1.)) =
      M33 (1., 0., 0., 0., 1., 0., 0., 0., 1.) in
  let t2 =
    inv_mat (M33 (1., 0., 0., 0., 2., 0., 0., 0., 3.)) =
      M33 (1., 0., 0., 0., 1./.2., 0., 0., 0., 1./.3.) in
  [t1; t2]

let matmul_tests =
  let t1 =
    let m = M33 (1., 2., 3., 4., 5., 6., 7., 8., 9.) in
    matmul_mat m m = M33 (30., 36., 42., 66., 81., 96., 102., 126., 150.) in
  let t2 =
    let m = M33 (0., 0., 0., 0., 0., 0., 0., 0., 0.) in
    matmul_mat m m = M33 (0., 0., 0., 0., 0., 0., 0., 0., 0.) in
  let t3 =
    let m = M33 (1., 1., 1., 1., 1., 1., 1., 1., 1.) in
    matmul_mat m m = M33 (3., 3., 3., 3., 3., 3., 3., 3., 3.) in
  [t1; t2; t3]

let () =
  assert (Utils.all_true nearly_eq_tests);
  assert (Utils.all_true all_true_tests);
  assert (Utils.all_true eq_point_tests);
  assert (Utils.all_true eq_mat_tests);
  assert (Utils.all_true det_mat_tests);
  assert (Utils.all_true trans_mat_tests);
  assert (Utils.all_true inv_mat_tests);
  assert (Utils.all_true matmul_tests);
  assert (Utils.all_true uniform_tests);
  assert (Utils.all_true array_linspace_test);
  assert (Utils.all_true list_linspace_test);
  print_endline "all the tests are passed"
