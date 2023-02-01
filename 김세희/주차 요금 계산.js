const getMinute = (time) => {
  const [hour, min] = time.split(":").map(Number);
  return hour * 60 + min;
};

function solution(fees, records) {
  var answer = [];
  const [defTime, defFee, rangeTime, rangeFee] = fees;
  const parkingLot = {};
  const totalTime = {};
  const totalFee = {};
  const endTime = getMinute("23:59");

  for (let record of records) {
    const [time, car, type] = record.split(" ");
    const totalMin = getMinute(time);
    if (type === "IN") {
      parkingLot[car] = [totalMin, true];
      if (!totalTime[car]) {
        totalTime[car] = 0;
      }
    } else {
      const start = parkingLot[car][0];
      const parkingTime = totalMin - start;
      totalTime[car] += parkingTime;
      parkingLot[car][1] = false;
    }
  }

  const restParking = Object.entries(parkingLot).filter(
    ([car, info]) => info[1]
  );

  for (const [car, info] of restParking) {
    const start = info[0];
    const parkingTime = endTime - start;
    totalTime[car] += parkingTime;
  }

  for (const [car, parkingTime] of Object.entries(totalTime)) {
    if (parkingTime <= defTime) {
      totalFee[car] = defFee;
    } else {
      totalFee[car] =
        defFee + Math.ceil((parkingTime - defTime) / rangeTime) * rangeFee;
    }
  }

  return Object.entries(totalFee)
    .sort((a, b) => +a[0] - b[0])
    .map(([car, fee]) => fee);
}
