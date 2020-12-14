let booking_info = {

  first_name: document.getElementById('first_name').value;
  last_name: document.getElementById('last_name').value;
  phone_number:document.getElementById('phone_number').value;
  email:document.getElementById('Email').value;
  bday_month: document.querySelector('bday_month').value;
  bday_day: document.querySelector('bday_day').value;
  bday_year: document.querySelector('bday_year').value;
  gym: document.querySelector('gym').value;
  booking_time: document.querySelector('booking_time').value;
  day_selection: document.querySelector('day_selection').value;

};

console.warn({booking_info});
