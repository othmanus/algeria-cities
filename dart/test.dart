import 'wilayat.dart';

main(List<String> args) {
  final alger = wilayat.firstWhere((wilaya) => wilaya['id'] == 16);
  print(alger);
  for (var daira in alger['dairas']) {
    print(daira['name']);
  }
}
