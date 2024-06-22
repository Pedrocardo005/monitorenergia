//import {Chart} from 'chart.js/auto';

const ctx = document.getElementById('myChart');
const title = document.getElementById('title');
const consumo = document.getElementById('consumo');
const select = document.getElementById('select');
const toArduino = document.getElementById('to-arduino');
const mockInformations = [];

let setIntervalReturn = 0;
      
let chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Gráfico com consumos',
            data: [],
            borderWidth: 1
        }]
    },
    options: {
        responsive: false,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    },
});

select.addEventListener('change', function (event) {
    let format_used = event.target.value;
    
    setIntervalReturn && clearInterval(setIntervalReturn);

    getData(format_used);

    setIntervalReturn = setInterval(() => {
        getData(format_used);
    }, 10000);    
});

function getData(format_used) {
    fetch(`formated/${format_used}/`)
        .then((response) => response.json())
        .then((response) => {
            const labels = response.items.map((element) => element.tempo);
            const data = response.items.map((element) => element.consumo);
            
            title.innerHTML = response.current_device;
            
            if (response.current_consumo) {
                consumo.innerHTML = `${response.current_consumo} W`;
            }
            
            chart.destroy();

            chart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Gráfico com consumos',
                        data: data,
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: false,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                },
            });
        });

}
    
toArduino.addEventListener('submit', function (event) {
    const value = document.getElementById('infos-arduino').value;

    event.preventDefault();
    
    fetch('send/arduino', {
        method: 'POST',
        body: JSON.stringify({value: value}),
    });
});
