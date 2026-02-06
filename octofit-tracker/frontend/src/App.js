

import logo from './logo192.png';
import './App.css';

function App() {
  return (
    <div>
      {/* Bootstrap Navigation */}
      <nav className="navbar navbar-expand-lg navbar-dark">
        <div className="container-fluid">
          <a className="navbar-brand d-flex align-items-center" href="#">
            <img src={logo} alt="OctoFit Logo" style={{height: '40px', marginRight: '12px', borderRadius: '8px', background: '#fff', padding: '2px'}} />
            OctoFit Tracker
          </a>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav ms-auto">
              <li className="nav-item">
                <a className="nav-link active" aria-current="page" href="#">Home</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#">Profile</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#">Teams</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#">Leaderboard</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <div className="container mt-5">
        <h1 className="display-4 mb-4 text-center">Welcome to OctoFit Tracker</h1>
        {/* Bootstrap Card Example */}
        <div className="row justify-content-center">
          <div className="col-md-6">
            <div className="card shadow">
              <div className="card-body">
                <h5 className="card-title">Get Started</h5>
                <p className="card-text">Track your fitness activities, join teams, and climb the leaderboard!</p>
                <a href="#" className="btn btn-primary">Log Activity</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
