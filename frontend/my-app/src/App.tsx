import React, { useState, useEffect } from "react";
import MatchRow from "./components/MatchRow";

const App: React.FC = () => {
  // Example matches for now
  const exampleMatches = [
    { id: "1", teamA: "Team A", teamB: "Team B", date: "2024-11-16", score: "2-1" },
    { id: "2", teamA: "Team C", teamB: "Team D", date: "2024-11-17", score: "1-1" },
    { id: "3", teamA: "Team E", teamB: "Team F", date: "2024-11-18", score: "3-2" },
    { id: "4", teamA: "Team G", teamB: "Team H", date: "2024-11-19", score: "0-0" },
    { id: "5", teamA: "Team I", teamB: "Team J", date: "2024-11-20", score: "1-0" },
  ];

  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold mb-6">Football Matches</h1>
      <table className="min-w-full bg-white border rounded shadow">
        <thead className="bg-gray-200">
          <tr>
            <th className="py-4 px-6 text-left">Team A</th>
            <th className="py-4 px-6 text-left">Team B</th>
            <th className="py-4 px-6 text-left">Date</th>
            <th className="py-4 px-6 text-left">Score</th>
            <th className="py-4 px-6 text-left">Stats</th>
          </tr>
        </thead>
        <tbody>
          {exampleMatches.map((match) => (
            <MatchRow key={match.id} match={match} />
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default App;
