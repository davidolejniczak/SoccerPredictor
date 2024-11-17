import React, { useState } from "react";

type MatchRowProps = {
  match: {
    id: string;
    teamA: string;
    teamB: string;
    date: string;
    score: string;
  };
};

const MatchRow: React.FC<MatchRowProps> = ({ match }) => {
  const [showStats, setShowStats] = useState(false);

  // Example stats for now
  const exampleStats = [
    { team_name: match.teamA, possession: "55%", shots: 10, fouls: 12 },
    { team_name: match.teamB, possession: "45%", shots: 5, fouls: 8 },
  ];

  const toggleStats = () => {
    setShowStats((prev) => !prev);
  };

  return (
    <>
      <tr className="border-b hover:bg-gray-100">
        <td className="py-4 px-6 font-medium">{match.teamA}</td>
        <td className="py-4 px-6 font-medium">{match.teamB}</td>
        <td className="py-4 px-6">{match.date}</td>
        <td className="py-4 px-6">{match.score}</td>
        <td className="py-4 px-6">
          <button
            onClick={toggleStats}
            className="bg-blue-500 text-white py-1 px-3 rounded hover:bg-blue-600"
          >
            {showStats ? "Hide Stats" : "Show Stats"}
          </button>
        </td>
      </tr>
      {showStats && (
        <tr>
          <td colSpan={5} className="bg-gray-100">
            <table className="min-w-full bg-gray-50 border rounded shadow mt-4">
              <thead>
                <tr className="bg-gray-200">
                  <th className="py-2 px-4 text-left">Team</th>
                  <th className="py-2 px-4 text-left">Possession</th>
                  <th className="py-2 px-4 text-left">Shots</th>
                  <th className="py-2 px-4 text-left">Fouls</th>
                </tr>
              </thead>
              <tbody>
                {exampleStats.map((stat, index) => (
                  <tr key={index} className="hover:bg-gray-100">
                    <td className="py-2 px-4 bg-white rounded text-center border">
                      {stat.team_name}
                    </td>
                    <td className="py-2 px-4 bg-white rounded text-center border">
                      {stat.possession}
                    </td>
                    <td className="py-2 px-4 bg-white rounded text-center border">
                      {stat.shots}
                    </td>
                    <td className="py-2 px-4 bg-white rounded text-center border">
                      {stat.fouls}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </td>
        </tr>
      )}
    </>
  );
};

export default MatchRow;
