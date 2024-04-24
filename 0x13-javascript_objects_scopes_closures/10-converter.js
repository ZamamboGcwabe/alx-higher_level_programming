#!/usr/bin/node

exports.converter = function (base) {
  return function (num) {
    if (num === 0) return '0';
    if (base === 1) return num.toString();

    const remainder = num % base;
    const quotient = Math.floor(num / base);
    const remainderChar = remainder < 10 ? remainder.toString() : String.fromCharCode(remainder + 55);
    return `${exports.converter(base)(quotient)}${remainderChar}`;
  };
};
