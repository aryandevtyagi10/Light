const tickets = [
  {
    match: "MI vs CSK",
    date: "April 15, 2025",
    stadium: "Wankhede Stadium",
    price: "₹1200",
    seat: "Block C2"
  },
  {
    match: "RCB vs KKR",
    date: "April 17, 2025",
    stadium: "Chinnaswamy Stadium",
    price: "₹900",
    seat: "East Stand"
  }
];

const ticketList = document.getElementById("ticketList");

tickets.forEach(ticket => {
  const ticketDiv = document.createElement("div");
  ticketDiv.classList.add("ticket");
  ticketDiv.innerHTML = `
    <h3>${ticket.match}</h3>
    <p><strong>Date:</strong> ${ticket.date}</p>
    <p><strong>Stadium:</strong> ${ticket.stadium}</p>
    <p><strong>Price:</strong> ${ticket.price}</p>
    <p><strong>Seat:</strong> ${ticket.seat}</p>
    <button onclick="alert('Proceeding to buy ${ticket.match} ticket')">Buy Now</button>
  `;
  ticketList.appendChild(ticketDiv);
});