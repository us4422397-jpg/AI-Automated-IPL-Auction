import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import DashboardLayout from './components/layout/DashboardLayout';
import Dashboard from './pages/Dashboard';
import PlayerAnalysis from './pages/PlayerAnalysis';
import TeamBuilder from './pages/TeamBuilder';
import AuctionRoom from './pages/AuctionRoom';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<DashboardLayout />}>
          <Route index element={<Navigate to="/dashboard" replace />} />
          <Route path="dashboard" element={<Dashboard />} />
          <Route path="players" element={<PlayerAnalysis />} />
          <Route path="team" element={<TeamBuilder />} />
          <Route path="auction" element={<AuctionRoom />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
