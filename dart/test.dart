import 'algeria_cites.dart';

main(List<String> args) {
  final alger = algeria_cites.firstWhere((wilaya) => wilaya['id'] == 16);
  print(alger);
  for (var daira in alger['dairas']) {
    print(daira['name']);
  }
}
