import {makeAutoObservable, runInAction } from "mobx";
// import {makeObservable, observable, action } from "mobx";
import mypageApi from "../api/MypageApi";

class FlightReserveStore{
  flight = {};
  flights = [];
  modalOpen = false;
  depart_airline = "";
  depart_dep_airport = "";
  depart_dest_airport = "";
  depart_etd = "";
  depart_eta = "";
  depart_et = "";
  depart_via = "";
  return_airline = "";
  return_dep_airport = "";
  return_dest_airport = "";
  return_etd = "";
  return_eta = "";
  return_et = "";
  return_via = "";
  imgUrl1 = "";
  imgUrl2 = "";
  price = "";
  oiCode="";
  cCode="";

  constructor() {
      makeAutoObservable(this, {}, { autoBind: true });
      this.selectAll();
    }

  // 로그인 구현끝나면 파라미터로 id 받아와야함
  async selectAll(){
    try {
      const results = await mypageApi.flightReserveList(1,'99','99');
      runInAction(() => this.flights = results);
      console.log(this.flights);
    } catch(error) {
      console.log(error);
    }
  }

  async deleteFlightReservation(){
    try {
      await mypageApi.flightReserveDelete(this.flight.id);
      this.flights = this.flights.filter(flight => flight.id !== this.flight.id);
      // console.log("###");
    } catch(error) {
      console.log(error);
    }
  }

  // 로그인 구현끝나면 파라미터로 id 받아와야함
  async selectFlightReservation(oi,c){
    try {
      const results = await mypageApi.flightReserveList(1,oi,c);
      runInAction(() => this.flights = results);
      console.log(this.flights);
    } catch(error) {
      console.log(error);
    }
    // console.log(oi, "###",c);
  }

  setFlight(flight){
    this.flight = flight;
    this.imgUrl1 = flight.flight_id.imgUrl1;
    this.imgUrl2 = flight.flight_id.imgUrl2;
    this.depart_airline = flight.flight_id.depart_airline;
    this.depart_dep_airport = flight.flight_id.depart_dep_airport;
    this.depart_dest_airport = flight.flight_id.depart_dest_airport;
    this.depart_etd = flight.flight_id.depart_etd;
    this.depart_eta = flight.flight_id.depart_eta;
    this.depart_et = flight.flight_id.depart_et;
    this.depart_via = flight.flight_id.depart_via;
    this.return_airline = flight.flight_id.return_airline;
    this.return_dep_airport = flight.flight_id.return_dep_airport;
    this.return_dest_airport = flight.flight_id.return_dest_airport;
    this.return_etd = flight.flight_id.return_etd;
    this.return_eta = flight.flight_id.return_eta;
    this.return_et = flight.flight_id.return_et;
    this.return_via = flight.flight_id.return_via;
    this.price = flight.flight_id.price;
    // console.log(this.room.room_id.name);
  }

  setModalOpen(isOpen){
    this.modalOpen = isOpen;
  }

  // setOiCode(oi){
  //   this.oiCode = oi;
  // }

  // setModal(c){
  //   this.cCode = c;
  // }
}

export default new FlightReserveStore();